import { Button, TextField, Box, Container } from "@mui/material";

function StudentAppealPopup({ student_state, student_setState }) {
  return (
    <Container>
      <TextField
        sx={{ m: 2 }}
        rows={15}
        multiline
        label="Treść podania"
      ></TextField>
      <Button sx={{ m: 2 }}>Wyślij</Button>
      <Button sx={{ m: 2 }} onClick={() => student_setState(!student_state)}>
        Wróć
      </Button>
    </Container>
  );
}

export default StudentAppealPopup;
