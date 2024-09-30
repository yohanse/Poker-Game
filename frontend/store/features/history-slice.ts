// f"Hand #{self.hand_id}\n{self.setup_data}\n{self.hole_cards}\n{self.actions}\n{self.winnings}"

import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import apiClient from "../../server/api-client";

export interface SimpleActionModel {
    type: string;
    amount: number | null;
    card: string | null;
}
interface History {
    id: string;
    stack: number;
    setup: string;
    hole_cards: string[][];
    winnings: number[];
    actions: SimpleActionModel[];
}

interface HistoryState {
    history: History[];
    status: string;
    error: string | null;
}

const initialState: HistoryState = {
    history: [],
    status: "idle",
    error: null
};

export const getAllHistory = createAsyncThunk("get all history", async () => {
    try {
        const response = await apiClient.get<History[]>("/hand-history");
        return response.data;
    }
    catch (error) {
        throw error;
    }
});


const historySlice = createSlice({
    name: "history",
    initialState,
    reducers: {

    },

    extraReducers(builder) {
        builder.addCase(getAllHistory.fulfilled, (state, action) => {
            state.history = [...action.payload]
            state.error = null
            state.status = "fulfilled"
        }).addCase(getAllHistory.pending, (state) => {
            state.history = [...state.history]
            state.error = null
            state.status = "pending"
        }).addCase(getAllHistory.rejected, (state, action) => {
            state.history = [...state.history]
            state.error = action.error.message ? action.error.message : null
            state.status = "rejected"
        });
    }

});

export default historySlice.reducer;