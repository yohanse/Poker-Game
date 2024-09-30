"use client";
import { Button } from '@/components/ui/button';

interface Props {
  name: string;
  disable: boolean;
  setClickedAction: (action: string) => void;
  value: number;
  setValue: (value: number) => void;
}

const IncrementDecrement = ({name, disable, setClickedAction, value, setValue}: Props) => {
  

  const handleIncrement = () => {
    setValue(value + 40);
  };
  
  const handleDecrement = () => {
    setValue(value > 40 ? value - 40 : 40); // Prevent negative numbers
  };

  const handleClicked = () => {
    setClickedAction(name);
  };

  return (
    <div className="flex gap-2 items-center justify-center">
      <Button onClick={handleDecrement} disabled={disable}>-</Button>
      <Button onClick={handleClicked} disabled={disable}>{name} {value}</Button>
      <Button onClick={handleIncrement} disabled={disable}>+</Button>
    </div>
  );
};

export default IncrementDecrement;
