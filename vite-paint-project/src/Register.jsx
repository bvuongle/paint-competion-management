import { alignProperty } from "@mui/material/styles/cssUtils";
import "./Register.css";
import {
  Box,
  Container,
  Paper,
  TextField,
  Button,
  Typography,
} from "@mui/material";

function Register() {
  return (
    <Container maxWidth="xs">
      <Paper elevation={4}>
        <p className="sign-in-text">Rejestracja</p>
        <Box
          component="form"
          display={"flex"}
          flexDirection={"column"}
          justifyContent="center"
          alignItems="center"
        >
          <TextField placeholder="Imię" required margin="dense"></TextField>
          <TextField
            placeholder="Nazwisko"
            required
            margin="dense"
            sx={{ mb: 3 }}
          ></TextField>
          <TextField placeholder="Login" required margin="dense"></TextField>
          <TextField placeholder="Hasło" required margin="dense"></TextField>
          <TextField
            placeholder="Potwierdź hasło"
            required
            margin="dense"
          ></TextField>
          <Button
            variant="contained"
            sx={{ margin: 2, backgroundColor: "#008000" }}
          >
            Rejestruj
          </Button>
          <Typography sx={{ my: 1 }}>Masz juz konto? Zaloguj się</Typography>
        </Box>
      </Paper>
    </Container>
  );
}

export default Register;
