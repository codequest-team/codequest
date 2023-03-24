export default function isValidDate(dateString) {
  if (dateString === null || dateString === "") return true;

  var regEx = /^\d{4}-\d{2}-\d{2}$/;
  if (!dateString.match(regEx)) return "Введите дату в формате гггг-мм-дд";

  var d = new Date(dateString);
  var dNum = d.getTime();
  if (!dNum && dNum !== 0) return "Неверно указана дата";

  return d.toISOString().slice(0, 10) === dateString || "Введите корректную дату";
}
