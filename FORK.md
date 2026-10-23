# Android 5.1 adapter

This `adapter/android-5.1` branch is a fork of the CleanYourTV launcher for one legacy TV:

- Hisense LED55MU7000U
- Android 5.1.1 / SDK 22
- Firmware `01.02.40.01`, UI version `JUUI 8.4.02.630`

The branch lowers the launcher `minSdk` to 22 and adds API-level fallbacks for fonts, locale access,
network callbacks, package-change queries, hardware bitmaps and older file APIs. It also contains an
opt-in boot receiver and a bundled wallpaper in the API-22 resource profile. The stock launcher stays
installed and enabled for recovery.

The owner reported that the launcher opened and injected four-way navigation worked on this TV. Physical
remote navigation, cold-boot handover, HDMI selection from the launcher and Live TV launch were not
validated. This branch is an Android 5.1 experiment; the upstream launcher still targets Android 8.0
(API 26) and newer.

The repository's Python wiring test passes locally. The Android Gradle build needs JDK 17 and was not run
in the current Windows environment because Java is unavailable.
