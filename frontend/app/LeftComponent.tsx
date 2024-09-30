"use client";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import IncrementDecrement from "./incremental_button";
import { useEffect, useState, useRef } from "react";
import { useAppDispatch, useAppSelector } from "@/store/hooks";
import { getActionStatus, postAction, resetActions } from "@/store/features/action-slice";
import { overGameRequest, startGameRequest, reset } from "@/store/features/start-slice";
import actionFormatter from "@/utils/action_to_string_converter";

interface GameState {
  selectedAction: string;
  isAfterAction: boolean;
}

const LeftComponent = () => {
  const [stack, setStack] = useState<number>(0);
  const [gameState, setGameState] = useState<GameState>({
    selectedAction: "",
    isAfterAction: false,
  });
  const [betValue, setBetValue] = useState<number>(40);
  const [raiseValue, setRaiseValue] = useState<number>(40);
  const scrollRef = useRef<HTMLDivElement | null>(null);

  // action states
  const action = useAppSelector((state) => state.action.action);
  const playingFieldLog = useAppSelector(
    (state) => state.action.playingFieldLog
  );

  // start states
  const start = useAppSelector((state) => state.start.start);
  const handleID = useAppSelector((state) => state.start.start?.id);

  //dispatch
  const dispatch = useAppDispatch();

  // Every time the data changes, scroll to the bottom
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [playingFieldLog]);

  // After action is done, get the avaliable actions
  useEffect(() => {
    const performAction = async () => {
      if (gameState.isAfterAction && handleID !== undefined) {
        console.log("Getting action status", handleID);
        await dispatch(getActionStatus(handleID!));
        setGameState({ selectedAction: "", isAfterAction: false });
      }
    };
    performAction();
  }, [gameState.isAfterAction]);



  // If it is either burning state, game over or deal state 
  useEffect(() => {
    const perform = async () => {
      if (action.burn) {
        await dispatch(
          postAction({
            action_type: "burn",
            hand_id: handleID!,
            stack: null,
            amount: null,
          })
        );
        setGameState({ selectedAction: "", isAfterAction: true });
      }
  
      if (action.deal) {
        await dispatch(
          postAction({
            action_type: "deal",
            hand_id: handleID!,
            stack: null,
            amount: null,
          })
        );
        setGameState({ selectedAction: "", isAfterAction: true });
      }
  
      if (action.gameOver) {
        await dispatch(overGameRequest(handleID!));
        setGameState({ selectedAction: "", isAfterAction: false });
      }
    };
    perform();
  }, [action.burn, action.deal, action.gameOver]);


  // Handle all the actions
  useEffect(() => {
    const perform = async () => {
      if (gameState.selectedAction === "start"){
        console.log("Start Button clicked !!!", stack);
        await dispatch(startGameRequest(stack));
        console.log("Start Button clicked !!!", handleID);
        setGameState({ selectedAction: "", isAfterAction: true });
      }
        
      else if (gameState.selectedAction === "reset"){
        dispatch(reset());
        dispatch(resetActions());
        setGameState({ selectedAction: "", isAfterAction: true });
      }

      else if (gameState.selectedAction !== ""){
        await dispatch(
          postAction({
            action_type: gameState.selectedAction,
            hand_id: handleID!,
            stack: null,
            amount:
              gameState.selectedAction == "bet"
                ? betValue
                : gameState.selectedAction == "raise"
                ? raiseValue
                : null,
          })
        );
        setGameState({ selectedAction: "", isAfterAction: true });
    };
  }
    perform();
}, [gameState.selectedAction]);

  

  

  return (
    <div className="w-1/2 bg-orange-800 px-10 py-5 flex flex-col gap-3">
      <div className="flex gap-4 justify-center">
        <div className="flex gap-4 items-center">
          <label htmlFor="stack">Stack</label>
          <Input
            className="h-9 w-20"
            type="number"
            placeholder="stack"
            id="stack"
            onChange={(event) => setStack(parseFloat(event.target.value))}
          />
        </div>
        <Button onClick={() => {
          if (handleID !== undefined) {
            setGameState({ selectedAction: "reset", isAfterAction: false });
          }
          else{
            setGameState({ selectedAction: "start", isAfterAction: false });
          }
        }}>{handleID !== undefined ? "Reset" : "Start"}</Button>
      </div>
      <div id="scrollableDiv" ref={scrollRef} className="bg-white flex-grow overflow-y-scroll no-scrollbar">
        {start &&
          start.hole_cards.map((value, index) => (
            <p key={index} className="text-black">
              Player {index + 1} is dealt {value[0]}
              {value[1]}
            </p>
          ))}
        <div>
          {start && <p className="text-black">Player 6 is the dealer</p>}
          {start && (
            <p className="text-black">Player 1 pots small blind - 20 chips</p>
          )}
          {start && (
            <p className="text-black">Player 2 pots small blind - 40 chips</p>
          )}
        </div>
        {playingFieldLog.map((value, index) => (
          <p key={index} className="text-black">
            {actionFormatter(value)}{" "}
          </p>
        ))}
        {start && (start.status === false ) && <div><p className="text-black">{`Hand #${start.id}`}</p><p className="text-black">{`Final pot was ${start.pot}`}</p></div>}
      </div>
      <div className="flex gap-3 items-center justify-center">
        <Button
          disabled={!action.fold}
          onClick={() => setGameState({ selectedAction: "fold", isAfterAction: false })}
        >
          Fold
        </Button>
        <Button
          disabled={!action.check}
          onClick={() => setGameState({ selectedAction: "check", isAfterAction: false })}
        >
          Check
        </Button>
        <Button
          disabled={!action.call}
          onClick={() => setGameState({ selectedAction: "call", isAfterAction: false })}
        >
          Call
        </Button>
        <IncrementDecrement
          value={betValue}
          setValue={setBetValue}
          disable={!action.bet}
          name="bet"
          setClickedAction={() => setGameState({ selectedAction: "bet", isAfterAction: false })}
        ></IncrementDecrement>
        <IncrementDecrement
          value={raiseValue}
          setValue={setRaiseValue}
          setClickedAction={() => setGameState({ selectedAction: "raise", isAfterAction: false })}
          disable={!action.raise}
          name="raise"
        ></IncrementDecrement>
        <Button
          disabled={!action.allIn}
          onClick={() => setGameState({ selectedAction: "allin", isAfterAction: false })}
        >
          All IN
        </Button>
      </div>
    </div>
  );
};

export default LeftComponent;
