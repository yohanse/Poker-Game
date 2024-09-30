"use client";

import { useEffect } from "react";
import { useAppDispatch, useAppSelector } from "@/store/hooks";
import { getAllHistory } from "@/store/features/history-slice";
import { HandHistoryCard } from "./HandHistoryCard";

const RightComponent = () => {
  const histories = useAppSelector((state) => state.history.history);
  const action = useAppSelector((state) => state.action.action);
  const error = useAppSelector((state) => state.history.error);
  const status = useAppSelector((state) => state.history.status);
  const dispatch = useAppDispatch();

  useEffect(() => {
      dispatch(getAllHistory());
  }, [action.gameOver]);
  return (
    <div className="w-1/2 h-full overflow-y-scroll no-scrollbar px-20 py-5 flex flex-col gap-4 scrollbar-none">
        <h1 className="">Hand History</h1>
        {histories.map((history, index) => (
          <HandHistoryCard
            key={index}
            setup_data={history.setup}
            hole_cards={history.hole_cards}
            actions={history.actions}
            winnings={history.winnings}
            hand_id={history.id} 
            stack={history.stack}>

            </HandHistoryCard>
        ))}
        {status === "pending" && <h1>Loading...</h1>}
        {error && <h1>{error}</h1>}
      </div>
  );
};

export default RightComponent;
