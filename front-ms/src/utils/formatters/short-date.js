export const shortDate = (date) => {
  /**
   * Функция возвращают конвертирует дату в формат -> 13 дек. 23г., 21:57:36
   */

  const options = {
    day: "2-digit",
    month: "short",
    year: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  };

  return new Intl.DateTimeFormat("ru-RU", options).format(new Date(date));
};