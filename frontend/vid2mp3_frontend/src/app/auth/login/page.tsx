"use client";

import { useState, ChangeEvent } from "react";
import { TextField, Button, Box, Typography, Link } from "@mui/material";
import axios from "axios";
import {z} from "zod";
import {useRouter} from "next/navigation";

const fieldSchema = z.object({
  email: z.string().email("Invalid Email Format"),
  password: z.string().min(1,"Password is required")
});

interface LoginForm {
  email: string;
  password: string;
}

export default function LoginPage() {
  const router = useRouter();

  const [form, setForm] = useState<LoginForm>({ email: "", password: "" });
  const [message, setMessage] = useState<string>("");

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    const result = fieldSchema.safeParse(form);

    if (!result.success) {
      setMessage(result.error.issues[0].message);
      return;
    }

    try {
      const res = await axios.post("http://localhost:8000/api/login", form);
      
      if (res.status === 200) {
        setMessage("Logged in successfully!");
        router.push("/home");
       } 

      // saving JWT from backend
      // localStorage.setItem("token", res.data.token);

    } catch (err) {
      setMessage("Login Failed!");
    }
  };

  return (
    <Box
      display="flex"
      flexDirection="column"
      maxWidth={400}
      mx="auto"
      mt={10}
      gap={2}
    >
      <Typography variant="h5">Login</Typography>

      <TextField
        label="Email"
        name="email"
        value={form.email}
        onChange={handleChange}
        required
      />

      <TextField
        type="password"
        label="Password"
        name="password"
        value={form.password}
        onChange={handleChange}
        required
      />

      <Typography>
        Don't have an account?{" "}
        <Link href="/auth/register" underline="hover">
          Register
        </Link>
      </Typography>
      <Button variant="contained" onClick={handleSubmit}>
        Login
      </Button>

      <Typography>{message}</Typography>
    </Box>
  );
}

