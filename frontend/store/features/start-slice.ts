import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import apiClient from "../../server/api-client";
import { useAppSelector } from "../hooks";

export interface Start {
    id: string;
    stack: number;
    setup: string;
    status: boolean;
    pot: number;
    hole_cards: string[][];
}

interface ActionState {
    start: Start | null;
    status: string;
    error: string | null;
}

const initialState: ActionState = {
    start: null,
    status: "idle",
    error: null
};

export const startGameRequest = createAsyncThunk("start game", async (stack: number) => {
    const response = await apiClient.post<Start>(`/game/start?stack=${stack}`);
    console.log(response.data);
    return response.data;
});

export const overGameRequest = createAsyncThunk("end game", async (hand_id: string) => {
    try {
        const response = await apiClient.get<Start>(`/game/over?hand_id=${hand_id}`);
        console.log(response.data);
        return response.data;
    }
    catch (error) {
        throw error;
    }
});

const startSlice = createSlice({
    name: "start",
    initialState,
    reducers: {
        reset() {
            return initialState;
        }
    },

    extraReducers(builder) {
        builder.addCase(startGameRequest.fulfilled, (state, action) => {
            state.start = {...action.payload};
            state.status = "fulfilled";
            state.error = null;
        }).addCase(startGameRequest.pending, (state) => {
            state.start = null;
            state.status = "pending";
            state.error =  null;
        }).addCase(startGameRequest.rejected, (state, action) => {
            state.start = null
            state.error = action.error.message ? action.error.message : null
            state.status = "rejected"
        });

        builder.addCase(overGameRequest.fulfilled, (state, action) => {
            state.start = {...action.payload}
            state.error = null
            state.status = "fulfilled"
        }).addCase(overGameRequest.pending, (state) => {
            state.error = null
            state.status = "pending"
        }).addCase(overGameRequest.rejected, (state, action) => {
            state.error = action.error.message ? action.error.message : null
            state.status = "rejected"
        });
    }

});

export const { reset } = startSlice.actions;
export default startSlice.reducer;