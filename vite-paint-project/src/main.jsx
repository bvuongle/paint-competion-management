import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import Login from "./Login.jsx";
import Register from "./Register.jsx";
import Jury from "./Jury.jsx";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Jury />
  </StrictMode>
);
