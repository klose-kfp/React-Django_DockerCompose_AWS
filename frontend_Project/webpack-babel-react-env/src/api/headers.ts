export default function authHeader() {
  const user = JSON.parse(localStorage.getItem("user") as string);
  // console.log(user.access);
  if (user && user.access) {
    return {
      Authorization: "JWT " + user.access,
      "Content-Type": "multipart/form-data",
    };
  } else {
    return {};
  }
}
