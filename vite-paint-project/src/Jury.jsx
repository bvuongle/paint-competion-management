import {
  Typography,
  Table,
  TableContainer,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  Paper,
} from "@mui/material";
import PowerSettingsNewIcon from "@mui/icons-material/PowerSettingsNew";
import "./Jury.css";

function createData(id, first_name, last_name, stage, grade, is_qualified) {
  return { id, first_name, last_name, stage, grade, is_qualified };
}

const rows = [
  createData(1, "John", "Doe", "II / Test pisemny", 80, "TAK"),
  createData(2, "Jan", "Nowak", "II / Test pisemny", 63, "NIE"),
];

function Jury() {
  return (
    <>
      <div className="top-bar">
        <div className="p-start">OLIMPIADA GEOGRAFICZNA</div>
        <PowerSettingsNewIcon className="user-icon" />
      </div>
      <p className="grades-header">WSZYSTKIE PRACE</p>
      {/* IDEA: make separate tables for first, second and third stages */}
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }}>
          <TableHead>
            <TableRow>
              <TableCell align="center">
                <b>Imię</b>
              </TableCell>
              <TableCell align="center">
                <b>Nazwisko</b>
              </TableCell>
              <TableCell align="center">
                <b>Etap / typ testu</b>
              </TableCell>
              <TableCell align="center">
                <b>Ocena</b>
              </TableCell>
              <TableCell align="center">
                <b>Czy przeszedł dalej</b>
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row.id}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell align="center">{row.first_name}</TableCell>
                <TableCell align="center">{row.last_name}</TableCell>
                <TableCell align="center">{row.stage}</TableCell>
                <TableCell align="center">{row.grade}</TableCell>
                <TableCell align="center">{row.is_qualified}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
}

export default Jury;
