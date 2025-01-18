import "./App.css";
// import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import PowerSettingsNewIcon from "@mui/icons-material/PowerSettingsNew";

function App() {
  return (
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
        <div className="grade">ocena: 89/100p. (89%)</div>
        <div className="step">próg: 88/100 (88%)</div>
        <div className="verdict">PRZECHODZISZ DALEJ</div>
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
  );
}

export default App;
