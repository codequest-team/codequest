export default function maxLength(val, maxLength) {
  return val === null || (val.match(/\n/g) || []).length + val.length <= maxLength || `Максимальная длина ${maxLength} символов`;
}