package com.gathin.tvhome;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class BootLaunchReceiverTest {
    private static final String BOOT_COMPLETED = "android.intent.action.BOOT_COMPLETED";

    @Test public void launchesOnlyForEnabledBootBroadcast() {
        assertTrue(BootLaunchReceiver.shouldLaunch(true, BOOT_COMPLETED));
        assertFalse(BootLaunchReceiver.shouldLaunch(false, BOOT_COMPLETED));
        assertFalse(BootLaunchReceiver.shouldLaunch(true, "android.intent.action.USER_UNLOCKED"));
        assertFalse(BootLaunchReceiver.shouldLaunch(true, null));
    }
}
