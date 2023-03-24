export default function minValue(val, min) {
  return val === null || val >= min || `Минимально допустимое число ${min}`;
}