"use client";

import {useState, ChangeEvent  } from "react";
import {TextField, Button, Box, Typography} from "@mui/material";
import axios from "axios";

interface RegisterForm{
  email: string;
  password: string;
}

export default function RegisterPage() {
  const [form, setForm] = useState<RegisterForm>({email:"", password:""});
  const [message, setMessage] = useState<string>("");

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setForm({...form, [e.target.name]: e.target.value});
  };

  const handleSubmit = async () => {
    try {
      
    } catch (error) {
      
    }
  };

  return (
  <Box>
  <Typography></Typography>
  <TextField/>
  <TextField/>
  <Button></Button>
  <Typography></Typography>
  </Box>
  );
}
