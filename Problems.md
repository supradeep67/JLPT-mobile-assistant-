# Technical Report: Mitigating AI Hallucination & Optimizing Edge Inference

This document outlines the architectural approach used to stabilize AI responses and optimize memory management within the RakuGEN mobile application. The primary challenge was addressing AI "hallucinations" and response loops without modifying the core C++ inference engine.

## 1. Problem Statement
The local LLM (Large Language Model) occasionally produced repetitive loops, irrelevant text (hallucinations), or exceeded memory limits on lower-end devices. Since the `LlamaBridge` is a pre-compiled library, optimizations had to be implemented at the Kotlin/UI layer.

## 2. Solution: Dynamic Parameter Tuning
Instead of static configuration, we implemented a reactive parameter system using `LlamaBridge.updateGenerateParams`. This allows the app to shift AI behavior based on the current mode (Fast vs. Deep Dive).

### Implementation Logic
We introduced strict constraints on "Creativity vs. Focus" by adjusting Temperature, Top-P, and Penalty parameters.

```kotlin
// Optimized Generation Parameters
LlamaBridge.updateGenerateParams(
    0.3f,           // Temperature: Low value (0.3) for higher predictability
    tokenLimit,     // Max Tokens: Dynamic limit based on Fast/Deep mode
    0.5f,           // Top-P: Nucleus sampling to filter out low-probability tokens
    20,             // Top-K: Limits vocabulary to top 20 choices for focus
    1.1f,           // Repeat Penalty: Prevents the AI from getting stuck in loops
    contextWindow,  // Context Length: User-adjustable via Settings slider
    4,              // Num Threads: Balanced for mobile CPU performance
    useMmap = true, // Memory Mapping: Loads model into RAM efficiently
    false,          // Flash Attention
    512             // Batch Size
)
```

## 3. Solution: User-Controlled Context Window
To manage device RAM and AI "memory," we implemented a dynamic Context Window slider. This allows users to decide how many tokens the AI should remember, directly impacting inference speed and stability.

### UI Implementation (Jetpack Compose)
A custom slider was integrated into the Settings sheet, allowing granular control over the `contextWindow` state.

```kotlin
var sliderValue by remember(contextWindow) { mutableFloatStateOf(contextWindow.toFloat()) }

SettingsSliderItem(
    icon = Icons.Default.Memory,
    label = "Context Window",
    description = "Token limit for AI memory (Performance vs. Recall)",
    value = sliderValue,
    valueRange = 1024f..8192f,
    steps = 7, // Increments of 1024
    onValueChange = { sliderValue = it },
    onValueChangeFinished = {
        scope.launch { settingsManager.setContextWindow(sliderValue.toInt()) }
    }
)
```

## 4. Prompt Engineering & Mode Switching
Hallucinations were further reduced by injecting "Guardrail" instructions into the system prompt based on the user's selected mode.

```kotlin
val systemPrompt = if (isFastMode) {
    "You are a 'Quick Reply' AI. Give short, one-sentence answers only. No intro."
} else {
    customBehavior.ifBlank { "You are a 'Deep Dive' AI. Provide detailed, comprehensive answers." }
}

// Applying the chat template to ensure structural integrity
val universalPrompt = LlamaBridge.applyChatTemplate(messages, true) ?: prompt
```

## 5. Summary of Benefits
*   **Stability**: Repeat penalty and low temperature virtually eliminated infinite loops.
*   **Resource Management**: The context slider prevents OOM (Out of Memory) crashes on older hardware.
*   **Zero C++ Overhead**: All improvements were achieved through the Kotlin high-level API, maintaining the portability of the core engine.

