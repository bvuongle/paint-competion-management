import { Button } from "@mui/material";
import "./Student.css";
import "./StudentAppealPopup.jsx";
import "./StudentAppealPopup.css";
// import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import PowerSettingsNewIcon from "@mui/icons-material/PowerSettingsNew";
import { useState } from "react";
import StudentAppealPopup from "./StudentAppealPopup.jsx";

function Student() {
  const [appeal, setAppeal] = useState(true);

  return appeal ? (
    <>
      <div className="top-bar">
        <div className="p-start">OLIMPIADA GEOGRAFICZNA</div>
        <PowerSettingsNewIcon className="user-icon" />
      </div>
      <p className="grades-header">TWOJE OCENY</p>
      <p className="p-stage-name oswald-font">Etap I</p>
      <div className="stage">
        <div className="test-type">Esej</div>
        <div className="grade">ocena: 96/100p. (96%)</div>
        <div className="step">próg: 83/100p. (83%)</div>
        <div className="verdict">PRZECHODZISZ DALEJ</div>
      </div>
      <p className="p-stage-name oswald-font">Etap II</p>
      <div className="stage">
        <div className="test-type">Test pisemny</div>
        <div className="grade">ocena: 93/100p. (93%)</div>
        <div className="step">próg: 87/100p. (87%)</div>
        <div className="verdict">ZAPRASZAMY NA TEST USTNY</div>
      </div>
      <div className="stage">
        <div className="test-type">Test ustny</div>
        <div className="grade">ocena: 82/100p. (82%)</div>
        <div className="step">próg: 88/100 (88%)</div>
        <div className="verdict">
          <Button
            onClick={() => setAppeal(!appeal)}
            title="Kliknij, aby złożyć apelację do Jury Konkursu"
            className="appeal-btn"
          >
            APELUJ
          </Button>
        </div>
      </div>
      {/*
      <p>
        Etap II --- Test ustny --- ocena: 87/100p. (87%) --- próg: 88/100 (88%) --- (przycisk) APELUJ
      </p>
      */}
      <p className="p-stage-name oswald-font">Etap III</p>
      <div className="stage">
        <div className="grade">ocena: 86/100 (86%)</div>
      </div>
    </>
  ) : (
    <StudentAppealPopup student_state={appeal} student_setState={setAppeal} />
  );
}

export default Student;
