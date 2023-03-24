export default function required(val) {
  return (val !== null && val !== "") || "Поле должно быть заполнено";
}