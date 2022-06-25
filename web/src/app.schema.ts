import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document } from 'mongoose';

export type AppDocument = App & Document;

@Schema()
export class App {
  @Prop()
  name: string;

  @Prop()
  price: number;

  @Prop()
  screenSize: string;

  @Prop()
  screenTechnology: string;

  @Prop()
  cpu: string;

  @Prop()
  ram: string;

  @Prop()
  internalMemory: string;

  @Prop()
  sim: string;
}

export const CatSchema = SchemaFactory.createForClass(App);
