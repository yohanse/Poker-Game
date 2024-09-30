import { configureStore } from "@reduxjs/toolkit";
import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import actionReducer from "./features/action-slice";
import historyReducer from "./features/history-slice";
import startReducer from "./features/start-slice";

export const store = configureStore({
    reducer: {
        action: actionReducer,
        history: historyReducer,
        start: startReducer,
    }
});

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
export type AppStore = typeof store