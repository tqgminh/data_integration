import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { ILike, Repository } from 'typeorm';
import { AppDto } from './app.dto';
import {
  Final,
  CellPhones,
  Didongviet,
  Dienmayxanh,
  FinalCellPhones,
  FinalDidongviet,
  FinalDienmayxanh,
  FinalTgdd,
  FinalTiki,
  FinalViettel,
  Tgdd,
  Tiki,
  Viettel,
} from './app.entity';

@Injectable()
export class AppService {
  constructor(
    @InjectRepository(Final)
    private readonly finalRepository: Repository<Final>,
    @InjectRepository(CellPhones)
    private readonly cellPhonesRepository: Repository<CellPhones>,
    @InjectRepository(Didongviet)
    private readonly didongvietRepository: Repository<Didongviet>,
    @InjectRepository(Dienmayxanh)
    private readonly dienmayxanhRepository: Repository<Dienmayxanh>,
    @InjectRepository(Tgdd)
    private readonly tgddRepository: Repository<Tgdd>,
    @InjectRepository(Tiki)
    private readonly tikiRepository: Repository<Tiki>,
    @InjectRepository(Viettel)
    private readonly viettelRepository: Repository<Viettel>,
    @InjectRepository(FinalViettel)
    private readonly finalViettelRepository: Repository<FinalViettel>,
    @InjectRepository(FinalCellPhones)
    private readonly finalCellPhonesRepository: Repository<FinalCellPhones>,
    @InjectRepository(FinalTiki)
    private readonly finalTikiRepository: Repository<FinalTiki>,
    @InjectRepository(FinalTgdd)
    private readonly finalTgddRepository: Repository<FinalTgdd>,
    @InjectRepository(FinalDienmayxanh)
    private readonly finalDienmayxanhRepository: Repository<FinalDienmayxanh>,
    @InjectRepository(FinalDidongviet)
    private readonly finalDidongvietRepository: Repository<FinalDidongviet>,
  ) {}

  async findAll(appDto: AppDto) {
    const { ten } = appDto;

    const rs = await this.finalRepository.find({
      where: { ten: ILike(`%${ten}%`) },
    });
    return rs;
  }

  async findInnerJoin(appDto: AppDto) {
    const { id } = appDto;
    const rs1 = await this.cellPhonesRepository
      .createQueryBuilder('cellPhones')
      .leftJoin('cellPhones.finalCellPhones', 'finalCellPhones')
      .leftJoin('finalCellPhones.final', 'final')
      .where('final.id=:id', { id })
      .getMany();

    const rs2 = await this.didongvietRepository
      .createQueryBuilder('didongviet')
      .leftJoin('didongviet.finalDidongviet', 'finalDidongviet')
      .leftJoin('finalDidongviet.final', 'final')
      .where('final.id=:id', { id })
      .getMany();

    const rs3 = await this.dienmayxanhRepository
      .createQueryBuilder('dienmayxanh')
      .leftJoin('dienmayxanh.finalDienmayxanh', 'finalDienmayxanh')
      .leftJoin('finalDienmayxanh.final', 'final')
      .where('final.id=:id', { id })
      .getMany();

    const rs4 = await this.tgddRepository
      .createQueryBuilder('tgdd')
      .leftJoin('tgdd.finalTgdd', 'finalTgdd')
      .leftJoin('finalTgdd.final', 'final')
      .where('final.id=:id', { id })
      .getMany();

    const rs5 = await this.tikiRepository
      .createQueryBuilder('tiki')
      .leftJoin('tiki.finalTiki', 'finalTiki')
      .leftJoin('finalTiki.final', 'final')
      .where('final.id=:id', { id })
      .getMany();

    const rs6 = await this.viettelRepository
      .createQueryBuilder('viettel')
      .leftJoin('viettel.finalViettel', 'finalViettel')
      .leftJoin('finalViettel.final', 'final')
      .where('final.id=:id', { id })
      .getMany();

    const rs = [...rs1, ...rs2, ...rs3, ...rs4, ...rs5, ...rs6];
    return rs;
  }

  async findOne(appDto: AppDto): Promise<Final> {
    const { ten } = appDto;
    return this.finalRepository.findOne({ where: { ten } });
  }
}
