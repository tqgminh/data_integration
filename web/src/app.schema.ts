import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document } from 'mongoose';

export type AppDocument = App & Document;

@Schema()
export class App {
  @Prop()
  ten: string;

  @Prop()
  gia_moi: number;

  @Prop()
  kich_thuoc_man_hinh: number;

  @Prop()
  cong_nghe_man_hinh: string;

  @Prop()
  cpu: string;

  @Prop()
  ram: number;

  @Prop()
  bo_nho_trong: number;

  @Prop()
  pin: number;

  @Prop()
  sim: string;
}

export const CatSchema = SchemaFactory.createForClass(App);
