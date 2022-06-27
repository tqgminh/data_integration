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
  screenSize: number;

  @Prop()
  screenTechnology: string;

  @Prop()
  cpu: string;

  @Prop()
  ram: number;

  @Prop()
  internalMemory: number;

  @Prop()
  sim: string;
}

export const CatSchema = SchemaFactory.createForClass(App);
