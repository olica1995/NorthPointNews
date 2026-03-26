package com.kyogatv.app

import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.android.exoplayer2.ExoPlayer
import com.google.android.exoplayer2.MediaItem
import com.google.android.exoplayer2.ui.PlayerView

class RadioPlayerActivity : AppCompatActivity() {

    private lateinit var player: ExoPlayer

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.player_layout)

        val playerView = findViewById<PlayerView>(R.id.player_view)

        player = ExoPlayer.Builder(this).build()
        playerView.player = player

        val mediaItem = MediaItem.fromUri(
            Uri.parse("https://stream.zeno.fm/4mb1wxhrefhvv.m3u")
        )

        player.setMediaItem(mediaItem)
        player.prepare()
        player.playWhenReady = true
    }

    override fun onStop() {
        super.onStop()
        player.release()
    }
}
