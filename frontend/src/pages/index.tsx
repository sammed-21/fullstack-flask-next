import Image from "next/image";
import { Inter } from "next/font/google";
import UserInterface from "@/components/UserInterface";

const inter = Inter({ subsets: ["latin"] });

const Home: React.FC = () => {
  return (
    <div className="flex w-full  min-h-screen justify-center items-center">
      <UserInterface backendName="backend" />
    </div>
  );
};

export default Home;
