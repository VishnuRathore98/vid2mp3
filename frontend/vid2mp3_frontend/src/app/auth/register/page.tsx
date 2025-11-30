"use client";

import { useState, ChangeEvent } from "react";
import { TextField, Button, Box, Typography, Link } from "@mui/material";
import axios from "axios";
import {z} from "zod";
import {useRouter} from "next/navigation";

const fieldSchema = z.object({
  full_name: z.string().min(1, "Name is required."),
  email: z.string().email("Invalid Email Format"),
  password: z.string().min(1,"Password is required")
});

interface RegisterForm {
  full_name: string;
  email: string;
  password: string;
}

export default function RegisterPage() {
  const router = useRouter();

  const [form, setForm] = useState<RegisterForm>({ full_name:"", email: "", password: "" });
  const [message, setMessage] = useState<string>("");

  // Handles input changes
  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Sends data to backend API
  const handleSubmit = async () => {
    const result = fieldSchema.safeParse(form);

    if (!result.success) {
      setMessage(result.error.issues[0].message);
      return;
    }

    try {
      const res = await axios.post("http://localhost:8000/auth/v1/register", form);

      if (res.status === 201) {
        setMessage("Registered Successfully!");
        router.push("/auth/login");
      }
    } catch (err) {
      setMessage("Registration Failed!");
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
      <Typography variant="h5">Register</Typography>

      <TextField
        label="Full name"
        name="full_name"
        value={form.full_name}
        onChange={handleChange}
        required
      />

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
        Already have an account?{" "}
        <Link href="/auth/login" underline="hover">Login</Link>
      </Typography>
      <Button variant="contained" onClick={handleSubmit}>
        Register
      </Button>

      <Typography>{message}</Typography>
    </Box>
  );
}

