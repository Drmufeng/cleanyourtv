# Hisense LED55MU7000U: Android 5.1.1 launcher experiment

This note records one owner's TV. It is not a tested debloat list or a statement that the reference
launcher supports Android 5.1.

| Field | Reported value |
|---|---|
| Retail model | Hisense LED55MU7000U |
| Market | China |
| Android / SDK | Android 5.1.1 / 22 |
| Firmware | `01.02.40.01` |
| TV UI version | `JUUI 8.4.02.630` |

## Advertising behavior

The boot ad remained after the TV's advertising preference was changed. That preference was restored to its original value (`0`). The firmware rejected the attempted `pm disable-user` request for the advertising service, so it remains enabled. Do not retry that request on this build.

## Launcher experiment

The reference launcher requires Android 8.0 (API 26), while this TV runs API 22. A local experimental
build lowered `minSdk` to 22, enabled core library desugaring, and added API-level fallbacks, including
system fonts below API 26. This is outside the repository's supported launcher baseline; it is not a
general Android 5.1 port, and other API-22 TVs may behave differently.

The API-22 build was installed and opened on this TV. The owner reports that the interface and
injected four-way navigation worked during the test. On this firmware, the cached hardware layer for
the focus glass could retain its previous bounds after focus changed; the experiment avoids that
layer on older Android and refits the glass after the launcher resumes.

The API-22 resource profile also opts into a bundled wallpaper, boot launch, and redirecting from
`com.jamdeo.tv.vod`. Those paths have not been verified on this TV: stock Home remains the default,
and cold-boot behavior is untested. Physical remote navigation, HDMI input selection from the
launcher, and Live TV launch have not been tested. Injected navigation does not establish that the
physical remote works. No Android firmware update was attempted.

Do not use this note as a package-disable list. No debloat list has been validated for this TV, and
the stock launcher has not been disabled.
