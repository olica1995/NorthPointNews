package com.kyogatv.app

import android.content.pm.ActivityInfo
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.android.exoplayer2.ExoPlayer
import com.google.android.exoplayer2.MediaItem
import com.google.android.exoplayer2.trackselection.DefaultTrackSelector
import com.google.android.exoplayer2.ui.PlayerView

class TvPlayerActivity : AppCompatActivity() {

    private lateinit var player: ExoPlayer
    private lateinit var trackSelector: DefaultTrackSelector
    private var isFullscreen = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.player_layout)

        val playerView = findViewById<PlayerView>(R.id.player_view)

        trackSelector = DefaultTrackSelector(this)

        player = ExoPlayer.Builder(this)
            .setTrackSelector(trackSelector)
            .setSeekBackIncrementMs(10000)
            .setSeekForwardIncrementMs(10000)
            .build()

        playerView.player = player

        val mediaItem = MediaItem.fromUri(
            Uri.parse("https://live21.bozztv.com/akamaissh101/ssh101/livetv1995/playlist.m3u8")
        )

        player.setMediaItem(mediaItem)
        player.prepare()
        player.playWhenReady = true

        playerView.setOnClickListener {
            toggleFullscreen()
        }
    }

    private fun toggleFullscreen() {
        requestedOrientation = if (isFullscreen)
            ActivityInfo.SCREEN_ORIENTATION_PORTRAIT
        else
            ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE

        isFullscreen = !isFullscreen
    }

    fun setVideoQuality(height: Int) {
        val params = trackSelector.buildUponParameters()
        when (height) {
            240 -> params.setMaxVideoSize(426, 240)
            480 -> params.setMaxVideoSize(854, 480)
            720 -> params.setMaxVideoSize(1280, 720)
            1080 -> params.setMaxVideoSize(1920, 1080)
        }
        trackSelector.setParameters(params)
    }

    override fun onStop() {
        super.onStop()
        player.release()
    }
}
