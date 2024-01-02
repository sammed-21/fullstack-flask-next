import { Card, CardContent, Typography } from "@mui/material";
import React from "react";

interface Card {
  id: number;
  name: string;
  email: string;
}
const CardComponent: React.FC<{ card: Card }> = ({ card }) => {
  return (
    <Card className="bg-black/90 text-white  max-w-[400px]">
      <CardContent>
        <Typography>{card.id}</Typography>
        <Typography>{card.name}</Typography>
        <Typography>{card.email}</Typography>
      </CardContent>
    </Card>
  );
};

export default CardComponent;
