export const drawCars = (ctx, width, height, laneWidth, stepSize, players) => {
  players.forEach(player => {
    ctx.shadowColor = "black";
    ctx.shadowBlur = 4;
    ctx.shadowOffsetX = 4;
    ctx.shadowOffsetY = 4;
    ctx.drawImage(player.carImage, laneWidth * player.id - laneWidth / 2 - 50, height - player.position * stepSize, 100, 80);
    ctx.shadowColor = "transparent";
  });
};