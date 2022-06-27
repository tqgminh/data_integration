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
    const { ten } = appDto;
    return this.AppModel.findOne({ ten }).exec();
  }

  async findByName(appDto: AppDto): Promise<App> {
    const { gia_moi } = appDto;
    return this.AppModel.findOne({ gia_moi }).exec();
  }

  async findByPrice(appDto: AppDto): Promise<App> {
    const { kich_thuoc_man_hinh } = appDto;
    return this.AppModel.findOne({ kich_thuoc_man_hinh }).exec();
  }

  async findByScreen(appDto: AppDto): Promise<App> {
    const { cong_nghe_man_hinh } = appDto;
    return this.AppModel.findOne({ cong_nghe_man_hinh }).exec();
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
    const { pin } = appDto;
    return this.AppModel.findOne({ pin }).exec();
  }

  async findBySim(appDto: AppDto): Promise<App> {
    const { sim } = appDto;
    return this.AppModel.findOne({ sim }).exec();
  }
}
