var VideoUtils = {
  makePosterFrameWithPlayButton: function(video) {
    var canvas, ctx, scaling;

    video = $(video)[0];

    canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    ctx = canvas.getContext('2d');

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.translate(canvas.width / 2, canvas.height / 2);

    // We want the play button to be 64x64px on an 800x600 video.
    // Scale it proportionally based on the actual size of our
    // video.
    scaling = canvas.width / 800;
    ctx.scale(scaling, scaling);

    ctx.fillStyle = 'rgba(255, 255, 255, 0.75)';
    ctx.beginPath();
    ctx.arc(0, 0, 64, 0, Math.PI * 2, false);
    ctx.fill();

    ctx.fillStyle = 'rgba(0, 0, 0, 0.66)';
    ctx.translate(16, 0);
    ctx.beginPath();
    ctx.moveTo(-32, -32);
    ctx.lineTo(16, 0);
    ctx.lineTo(-32, 32);
    ctx.fill();

    return canvas.toDataURL('image/jpeg', 0.8);
  },
  waitForFrame: function(video, cb) {
    video = $(video);

    if (video[0].readyState < 2) {
      video.one('canplay', cb);
    } else {
      setTimeout(function() {
        cb.call(video[0]);
      }, 0);
    }
  }
};
