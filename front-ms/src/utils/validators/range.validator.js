export default function range(val, min, max) {
  return val === null || (val >= min && val <= max) || `Введите число от ${min} до ${max}`;
}
