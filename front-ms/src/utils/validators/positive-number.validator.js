export default function positiveNumber(val) {
  if (typeof val === "string" && val) {
    if (!val.match(/^\d+$/) && !val.match(/^\d+\.\d+$/))
      return "Введите положительное число";

    if (typeof val === "string" && val.match(/^\d+\,\d+$/))
      return "Используйте точку вместо запятой";
  }

  return val === "" || val === null || val >= 0 || "Введите положительное число";
}
