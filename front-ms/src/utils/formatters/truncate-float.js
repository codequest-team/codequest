export const truncateFloat = (number, digits = 1) => {
  /**
   * Функция обрезает вещественное число оставляя указанное
   * кол-во чисел после запятой без округления
   */

  if (number % 1 === 0) return number;

  number = number.toString();

  return parseFloat(number.substring(0, number.indexOf(".") + 1 + digits));
};