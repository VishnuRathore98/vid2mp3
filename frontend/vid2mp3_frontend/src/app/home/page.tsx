"use client";

import {Box, Typography, Button} from "@mui/material";
import {useRouter} from "next/navigation";

export default function HomePage() {
  const router = useRouter(); 

  var username="test";

  const handleLogout = () => {
    router.push("/auth/login");
  };

  return (
    <Box 
    display="flex"
      flexDirection="column"
      maxWidth={600}
      mx="auto"
      mt={10}
      gap={3}
    >
      <Typography variant="h4">Welcome home {username}.</Typography>
      <Typography variant="body1">You are logged in successfully!</Typography>
      <Button variant="contained" onClick={handleLogout}>Logout</Button>
    </Box>
  );
}
