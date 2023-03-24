function drawText(ctx, text, x, y, fontSize = '14px', fontFace = 'Arial', fillColor = '#ccc') {
  ctx.font = `${fontSize} ${fontFace}`; // задаем размер и тип шрифта
  ctx.fillStyle = fillColor; // выбираем цвет заливки текста
  ctx.fillText(text, x, y); // рисуем текст с заданными координатами
}

export const drawUsernames = (ctx, width, height, laneWidth, players) => {
  ctx.globalAlpha = 0.7; // устанавливаем значение прозрачности (0 - полностью прозрачный, 1 - непрозрачный)
  ctx.fillStyle = "#374151"; // выбираем цвет заливки
  ctx.fillRect(0, height - 20, width, height); // рисуем прямоугольник с заданными координатами и размерами
  ctx.globalAlpha = 1; // возвращаем значение прозрачности к непрозрачному состоянию

  let x = 15;
  players.forEach(player => {
    const username = player.username.length > 8 ? player.username.substr(0, 8) + "..." : player.username;
    drawText(ctx, username, x, height - 5);
    x += laneWidth;
  });
};

