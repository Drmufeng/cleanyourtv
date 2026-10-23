package com.gathin.tvhome;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

/** Starts the launcher after boot on legacy firmware that starts its own home directly. */
public final class BootLaunchReceiver extends BroadcastReceiver {

    static boolean shouldLaunch(boolean enabled, String action) {
        return enabled && Intent.ACTION_BOOT_COMPLETED.equals(action);
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent == null || !shouldLaunch(
                context.getResources().getBoolean(R.bool.launch_after_boot), intent.getAction())) return;

        Intent launch = new Intent(context, MainActivity.class)
                .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED);
        context.startActivity(launch);
    }
}
