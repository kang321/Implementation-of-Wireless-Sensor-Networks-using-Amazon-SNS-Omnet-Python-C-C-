import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.contract.INetworkNode;
import inet.physicallayer.wireless.common.contract.packetlevel.IRadioMedium;
import inet.visualizer.contract.IIntegratedVisualizer;
import inet.node.aodv.AodvRouter;

network test
{
    parameters:
        @display("bgb=695,454;bgi=showcases/default,s");
        @figure[title](type=label; pos=0,-1; anchor=sw; color=darkblue);
        @figure[r1](type=indicatorText; pos=400,40; anchor=w; font=,12; textFormat="pcks rcvd from Smoke Sensor: %g"; initialValue=0);
        @statistic[packetReceivedFromUpper1](source=hostR1.udp.packetSent; record=figure(count); targetFigure=r1);
        
        @figure[rcvdPkText2](type=indicatorText; pos=400,120; anchor=w; font=,12; textFormat="pcks rcvd from Camera Sensor: %g"; initialValue=0);
        @statistic[packetReceivedFromUpper](source=hostB.app[0].packetSent; record=figure(count); targetFigure=rcvdPkText2);

        @figure[rcvdPkText3](type=indicatorText; pos=400,60; anchor=w; font=,12; textFormat="pcks rcvd from Humidity Sensor: %g"; initialValue=0);
        @statistic[packetReceivedFromUpper2](source=hostD.app[0].packetSent; record=figure(count); targetFigure=rcvdPkText3);

        @figure[rcvdPkText5](type=indicatorText; pos=400,80; anchor=w; font=,12; textFormat="pcks rcvd from Temp Sensor: %g"; initialValue=0);
        @statistic[packetReceivedFromUpper3](source=hostE.app[0].packetSent; record=figure(count); targetFigure=rcvdPkText5);

        @figure[rcvdPkText6](type=indicatorText; pos=400,100; anchor=w; font=,12; textFormat="pcks rcvd from Co2 Sensor: %g"; initialValue=0);
        @statistic[packetReceivedFromUpper4](source=hostF.app[0].packetSent; record=figure(count); targetFigure=rcvdPkText6);

    submodules:
        visualizer: <default(firstAvailableOrEmpty("IntegratedCanvasVisualizer"))> like IIntegratedVisualizer if typename != "" {
            @display("p=643,323");
        }
        configurator: Ipv4NetworkConfigurator {
            @display("p=645,255");
        }
        radioMedium: <default("UnitDiskRadioMedium")> like IRadioMedium {
            @display("p=648,194");
        }
        hostA: <default("WirelessHost")> like INetworkNode {
            @display("p=47,88;i=misc/fire");
        }
        hostC: <default("WirelessHost")> like INetworkNode {
            @display("p=290,198;i=misc/sensorgateway");
        }
        hostB: <default("WirelessHost")> like INetworkNode {
            @display("p=48,365;i=misc/securitycamera");
        }
        hostR2: <default("WirelessHost")> like INetworkNode {
            @display("p=115,347;i=device/accesspoint");
        }
        hostR1: <default("WirelessHost")> like INetworkNode {
            @display("p=103,87;i=device/accesspoint");
        }
        hostA1: <default("WirelessHost")> like INetworkNode {
            @display("p=98,49;i=misc/fire");
        }
        hostA2: <default("WirelessHost")> like INetworkNode {
            @display("p=51,50;i=misc/fire");
        }
        hostR3: <default("WirelessHost")> like INetworkNode {
            @display("p=317,100;i=device/accesspoint");
        }
        hostD: <default("WirelessHost")> like INetworkNode {
            @display("p=373,58;i=misc/humid");
        }
        hostE: <default("WirelessHost")> like INetworkNode {
            @display("p=409,400;i=misc/thermometer;is=l");
        }
        hostR4: <default("WirelessHost")> like INetworkNode {
            @display("p=365,401;i=device/accesspoint");
        }
        hostF: <default("WirelessHost")> like INetworkNode {
            @display("p=438,152;i=misc/carbon-dioxide-sensor");
        }
        hostR5: AodvRouter {
            @display("p=376,192;i=device/accesspoint");
        }
}
