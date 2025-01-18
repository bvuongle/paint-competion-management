import { alignProperty } from "@mui/material/styles/cssUtils";
import "./Login.css";
import {
  Box,
  Container,
  Paper,
  TextField,
  Button,
  Typography,
} from "@mui/material";

function Login() {
  return (
    <Container maxWidth="xs">
      <Paper elevation={4}>
        <p className="sign-in-text">Logowanie</p>
        <Box
          component="form"
          display={"flex"}
          flexDirection={"column"}
          justifyContent="center"
          alignItems="center"
        >
          <TextField placeholder="Login" required margin="dense"></TextField>
          <TextField placeholder="Hasło" required margin="dense"></TextField>
          <Button
            variant="contained"
            sx={{ margin: 2, backgroundColor: "#008000" }}
          >
            Zaloguj
          </Button>
          <Typography sx={{ my: 1 }}>
            Nie masz konta? Zarejestruj się
          </Typography>
        </Box>
      </Paper>
    </Container>
  );
}

export default Login;
