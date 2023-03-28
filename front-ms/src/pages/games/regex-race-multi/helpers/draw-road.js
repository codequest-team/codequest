export const drawRoad = (ctx, width, height, laneCount, laneWidth, stepSize) => {
  ctx.strokeStyle = "#facc15";
  ctx.beginPath();
  ctx.setLineDash([]);
  ctx.moveTo(0, 0);
  ctx.lineTo(0, height);
  ctx.moveTo(width, 0);
  ctx.lineTo(width, height);
  ctx.lineWidth = 15;
  ctx.stroke();

  // Цвет линий
  ctx.strokeStyle = "#f8fafc";

  // Начальная точка для первой линии
  let x = laneWidth;

  // Нарисовать 3 линии с интервалом в 100px
  for (let i = 0; i < laneCount - 1; i++) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, height);
    ctx.setLineDash([10, 10]);
    ctx.lineWidth = 0.5;
    ctx.stroke();
    x += laneWidth;
  }

  const lineWidth = 5; // ширина линии
  const lineLength = width; // длина линии равна ширине холста

  function drawHorizontalStripes(y, startWithWhite) {
    let isWhite = startWithWhite; // флаг, указывающий на цвет текущей полосы

    for (let i = 8; i < lineLength - 8; i += lineWidth) {
      ctx.beginPath();
      ctx.moveTo(i, y);
      ctx.lineTo(i + lineWidth, y);
      ctx.lineWidth = lineWidth;
      ctx.strokeStyle = isWhite ? "#f8fafc" : "#374151";
      ctx.stroke();
      isWhite = !isWhite; // меняем флаг цвета на противоположный
    }
  }

  drawHorizontalStripes(stepSize, true);
  drawHorizontalStripes(stepSize + 5, false);
};
