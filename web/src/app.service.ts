import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { AppDto } from './app.dto';
import { App, AppDocument } from './app.schema';

@Injectable()
export class AppService {
  constructor(
    @InjectModel(App.name) private readonly AppModel: Model<AppDocument>,
  ) {}

  async findAll(): Promise<App[]> {
    return this.AppModel.find().exec();
  }

  async findOne(appDto: AppDto): Promise<App> {
    const { name } = appDto;
    return this.AppModel.findOne({ name }).exec();
  }

  async findByName(appDto: AppDto): Promise<App> {
    const { price } = appDto;
    return this.AppModel.findOne({ price }).exec();
  }

  async findByPrice(appDto: AppDto): Promise<App> {
    const { screenSize } = appDto;
    return this.AppModel.findOne({ screenSize }).exec();
  }

  async findByScreen(appDto: AppDto): Promise<App> {
    const { screenTechnology } = appDto;
    return this.AppModel.findOne({ screenTechnology }).exec();
  }

  async findByCpu(appDto: AppDto): Promise<App> {
    const { cpu } = appDto;
    return this.AppModel.findOne({ cpu }).exec();
  }

  async findByRam(appDto: AppDto): Promise<App> {
    const { ram } = appDto;
    return this.AppModel.findOne({ ram }).exec();
  }

  async findByBattery(appDto: AppDto): Promise<App> {
    const { battery } = appDto;
    return this.AppModel.findOne({ battery }).exec();
  }

  async findBySim(appDto: AppDto): Promise<App> {
    const { sim } = appDto;
    return this.AppModel.findOne({ sim }).exec();
  }
}
