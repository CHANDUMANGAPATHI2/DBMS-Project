import express from "express";
import * as taskservice from "../services/taskService.js";

const router=express.Router();
router.post("/createtask",async (req,res)=>{
    res.json(await taskservice.createTask(req.body, req.headers["token"]));
});
export default router;