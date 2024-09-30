"use client";

import LeftComponent from "./LeftComponent";
import RightComponent from "./RightComponent";


export default function Home() {
  return (
    <div className="flex gap-1 h-screen w-screen">
      <LeftComponent></LeftComponent>
      <RightComponent></RightComponent>
    </div>
  );
}
