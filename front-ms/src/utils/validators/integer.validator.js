export default function integer(val) {
  return val === null || val % 1 === 0 || "Введите целое число";
}