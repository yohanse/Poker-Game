import { createSlice } from "@reduxjs/toolkit";
import { createAppAsyncThunk } from "../create-async-thunk";
import apiClient from "../../server/api-client";

interface Action {
    check: boolean,
    call: boolean,
    bet: boolean,
    raise: boolean,
    burn: boolean,
    fold: boolean,
    gameOver: boolean,
    allIn: boolean,
    deal: boolean
}

interface ActionPostItem {
    action_type: string,
    hand_id: string | null,
    stack: number | null,
    amount: number | null
}

export interface ActionPostItemResponse {
    id: string,
    player: number,
    type: string,
    card: string,
    amount: number
}

interface ActionState {
    action: Action;
    playingFieldLog: ActionPostItemResponse[];
    status: 'idle' | 'pending' | 'succeeded' | 'failed';
    error: string | null;
}

const initialState: ActionState = {
    action: {
        allIn: false,
        call: false,
        check: false,
        bet: false,
        raise: false,
        burn: false,
        fold: false,
        gameOver: false,
        deal: false
    },
    playingFieldLog: [],
    status: "idle",
    error: null
};

export const getActionStatus = createAppAsyncThunk("getAction", async (hand_id: string) => {
    const response = await apiClient.get<Action>(`/game/actions?hand_id=${hand_id}`);
    console.log(response.data);
    return response.data;
});

export const postAction = createAppAsyncThunk("postAction", async (actionPostItem: ActionPostItem) => {
    const response = await apiClient.post<ActionPostItemResponse>("/game/actions", actionPostItem);
    console.log(response.data);
    return response.data;
});

const actionSlice = createSlice({
    name: "action",
    initialState,
    reducers: {
        resetActions() {
            return initialState;
        }
    },

    extraReducers(builder) {
        builder.addCase(getActionStatus.fulfilled, (state, action) => {
            state.action = {...action.payload};
            state.error = null;
            state.status = "succeeded";
        }).addCase(getActionStatus.pending, (state) => {
            state.action = {
                    check: false,
                    call: false,
                    deal: false,
                    allIn: false,
                    bet: false,
                    raise: false,
                    burn: false,
                    fold: false,
                    gameOver: false,};
            state.status = "pending";
        }).addCase(getActionStatus.rejected, (state, action) => {
        state.error = action.error.message ? action.error.message : null,
        state.status = "failed";
        });

        builder.addCase(postAction.fulfilled, (state, action) => {
            state.action = {
                check: false,
                call: false,
                deal: false,
                allIn: false,
                bet: false,
                raise: false,
                burn: false,
                fold: false,
                gameOver: false,
            };
            state.playingFieldLog = [...state.playingFieldLog, action.payload],
            state.error = null,
            state.status = "succeeded"
        }).addCase(postAction.pending, (state) => {
            state.action = {
                check: false,
                call: false,
                deal: false,
                allIn: false,
                bet: false,
                raise: false,
                burn: false,
                fold: false,
                gameOver: false,
            };
            state.playingFieldLog = [...state.playingFieldLog],
            state.error = null,
            state.status = "pending"
            
        }).addCase(postAction.rejected, (state, action) => {
            state.action = {
                check: false,
                call: false,
                deal: false,
                allIn: false,
                bet: false,
                raise: false,
                burn: false,
                fold: false,
                gameOver: false,
            };
            state.status = "failed";
            state.error = action.error.message ? action.error.message : null;
        });
    }

});

export const { resetActions } = actionSlice.actions;
export default actionSlice.reducer;