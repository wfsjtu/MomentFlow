# Add project specific ProGuard rules here.
-keepattributes *Annotation*
-keepclassmembers class * {
    @dagger.hilt.android.internal.lifecycle.HiltViewModel <fields>;
}
