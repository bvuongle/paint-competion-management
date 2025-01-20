import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import "./index.css";
import Student from "./Student.jsx";
import Login from "./Login.jsx";
import Register from "./Register.jsx";
import Jury from "./Jury.jsx";

import Test from "./Test.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Student />
  </StrictMode>
);
