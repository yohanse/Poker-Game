'use client';
import { Provider } from "react-redux";
import { store } from "@/store/store";
import { ReactNode } from "react";

interface Props {
  children: ReactNode; // Use ReactNode to type children properly
}

const provider = ({ children } : Props) => {
  return <Provider store={store}>{children}</Provider>;
}

provider.displayName = "Provider";

export default provider;
